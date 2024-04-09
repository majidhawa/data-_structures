import heapq

numbers = [ 4,9,5,9,3,6,8,1,2,7]

#Negate each element to convert max heap
numbers=[-x for x in numbers]

    # Create a min heap
heapq.heapify(numbers)

    # Accessing the min item
max_item = numbers[0]

print("Max item:",max_item)

    # Accessing other items 
for item in numbers:
    print("Item in heap:",item)