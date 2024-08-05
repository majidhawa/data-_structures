#To insert an element into a heap
def heapify_up(heap, index):
    parent_index = (index - 1) // 2
    if index > 0 and heap[index] > heap[parent_index]:  
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        heapify_up(heap, parent_index)

def insert(heap, element):
    heap.append(element)
    heapify_up(heap, len(heap) - 1)


heap = [10, 5, 3, 2, 4]
insert(heap, 15)
print(heap)  


##To delete the maximum (or minimum) element from a heap
def heapify_down(heap, index):
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    largest = index
    
    if left_child_index < len(heap) and heap[left_child_index] > heap[largest]:  # For a max heap
        largest = left_child_index
    if right_child_index < len(heap) and heap[right_child_index] > heap[largest]:
        largest = right_child_index
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        heapify_down(heap, largest)

def delete_max(heap):
    if len(heap) == 0:
        return None
    max_element = heap[0]
    heap[0] = heap.pop()
    heapify_down(heap, 0)
    return max_element


heap = [15, 10, 3, 2, 4, 5]
max_element = delete_max(heap)
print(max_element)  
print(heap)         

##Implementing a heap using array
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def delete_max(self):
        if len(self.heap) == 0:
            return None
        max_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_element

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(3)
heap.insert(2)
heap.insert(4)
heap.insert(15)
print(heap.heap)  
max_element = heap.delete_max()
print(max_element)  
print(heap.heap)    

