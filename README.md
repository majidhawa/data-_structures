Heaps

Heaps are a type of binary tree based data structures constrained by a heap property
They are nearly complete  binary tree.
There are two types of heap:
  Min heap
  Max heap
Advantages of using heaps
  Efficient insertion and deletion
  Guaranteed access to max and min element
  Space efficiency

Disadvantages of using heaps
 Lack of flexibility 
 Not suitable for sorting
 Inefficient for searching
 Not certain for certain operations like finding median

Applications of a heap
 Used to implement priority queues
 Selection Algorithm e.g finding the smallest element in a list
 Used in allocating and deallocating memory dynamically
 Used in various algorithm such as Dijkstra to find the node of the smallest 




 TUPLE

A tuple is an ordered and finite list of elements, which can be of various types and can include duplicates.  Tuples are similar to arrays and list but are immutable ,meaning their values cannot be changed after they are created.Tuples have limited functionality due to their immutability. THey do not have methods of adding, updating  or removing items.




Properties of  a Tuple



Ordered -  Tuples maintain the order of elements as they were added. 
Immutable- Once a tuple is created , it cannot be changed. This includes adding ,removing or modifying elements
Lightweight- Tuples are more memory-efficient than lists , especially when storing a large number of elements.
Indexable- Tuples can be indexed using zero based indexing ,allowing you to accessing elements by their position in tuple
Heterogenous Tuples can store elements of different data types. This means you can have a tuple that contains a integers, strings and other tuples
Nestable- Tuples can contain other tuples  allowing complex data structures like tuples of tuples
Iterable- Tuples are iterable, meaning you can loop over their elements. 
Sliceable- Tuples support slicing allowing you to extract a portion of tuple



Advantages of Tuples


They are immutable making them safer to use  in crucial data as they cannot be modified
They do not require extra spaces for storing their size and capacity
Are faster than list when it comes to accessing and iterating over their elements due to their small memory 
Can be used as keys in dictionaries since they are immutable
Tuples maintain the order of the elements which is useful for tasks that requires elements to be in specific sequence




Disadvantages of Tuples



It is difficult to remove elements from them
Has fewer inbuilt functions and methods which makes them less convenient to work with.
They are less flexible compared to list  because they can not modified after creation.





Application of Tuple



They are used to represent data records, where each record is an ordered and unchangeable sequence of objects
They are used to data where data integrity is crucial such as configuration setting or defining constants
Used as keys in dictionaries where each key is a tuple representing a unique combination of values
Tuples can contain other tuples allowing creation 




Deleting and inserting items in tuples



In Python,tuples are immutable, meaning their elements cannot be modified once created. Attempting to directly update a tuple element will result in a TypeError. However, there are techniques to simulate updating a tuple by creating a new tuple with the desired changes without modifying the original tuple directly. This includes:
Using Packing/Unpacking
Using Tuple Slicing
Using List Comprehension














