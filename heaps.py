import heapq

numbers = [ 4,9,5,10,3,6,8,1,2,7]

#Create a min heap
heapq.heapify(numbers)

#Accessing the min item

min_item= numbers[0]

print("Min item: ",min_item)



#Deleting an item in min heap
heapq.heappop(numbers)
print(numbers)

#Adding an item on the max heap

heapq.heappush(numbers,5)
print(numbers)





# numbers = [ 4,9,10,3,6,8,1,2,7]

# #Negate each element to convert max heap
# numbers=[-x for x in numbers]

#     # Create a min heap
# heapq.heapify(numbers)

#     # Accessing the max item
# max_item = numbers[0]

# print("Max item:",max_item)


# #Deleting an item in max heap
# heapq.heappop(numbers)
# print(numbers)


# #Accessing more than one item from the smallest values
# smallest_values = heapq.nsmallest(3,numbers)
# print(smallest_values)


# #Accessing more than one item from the largest values
# highest_values = heapq.nlargest(4,numbers)
# print(highest_values)

# #Adding an item on the max heap

# heapq.heappush(numbers,-5)
# print(numbers)
