my_tuple = (1, "red","mango",2, "orange",3)

# Accessing the first element
print(my_tuple[0]) 

# Accessing the last element
print(my_tuple[-1])
 



# Convert the tuple to a list
tuple_list = list(my_tuple)

# Update a specific element

tuple_list[2] =35

# Convert the list back to a tuple
new_tuple = tuple(tuple_list)
print("Original Tuple:", my_tuple)
print("Updated Tuple:", new_tuple)