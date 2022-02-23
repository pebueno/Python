#Collection structures

#METHODS

fruits = ["Apple", "Banana", "Avocado","Quince","Grape"]
print(fruits)
print(fruits[4])
print(type(fruits))

# .len() method returns the length of the list
print(len(fruits))

# .append() method is used to add elements at the end of the list 
fruits.append("Quince")

# .insert() method can add an element at a given position in the list 
fruits.insert(0, "Star fruit")

fruits[3] = "Pear"
# .extend() method is used to add more than one element at the end of the list
fruits.extend(["Orange", "Lemon"]) 

# .remove() method is used to remove an element from the list
fruits.remove("Lemon")


# .pop() method can remove an element from any position in the list 
fruits.pop(0)

# The min() method returns the minimum value in the list
print(min(fruits))
# The max() method returns the maximum value in the list
print(max(fruits))

numbers = [1, 2, 3]
print(min(numbers))
print(max(numbers))

# .sort() method sorts the list in ascending order
fruits.sort()
print(fruits)

#OPERATIONS

# Concatenate operation is used to merge two lists and return a single list
print(fruits+numbers) 

# Slice operation is used to print a section of the list 
print(fruits[:4])  # prints from beginning to end index
print(fruits[2:])  # prints from start index to end of list
print(fruits[2:4]) # prints from start index to end index
print(fruits[:])   # prints from beginning to end of list

# Reverse operation is used to reverse the elements of the list
fruits.reverse()
print(fruits)

# Multiply the list n times 
print(fruits*5)

#FUNCTIONS

# function count() returns the number of occurrences of a given element in the list.
print(fruits.count(0))