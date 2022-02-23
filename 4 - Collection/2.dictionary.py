# Define a dictionary
products = { 'Fresh Oil': 500, 'Mango Juice': 30, '5 star Chocalate': 20, 'Pedro Fruit Cake': 50 }
me = {'name': 'Pedro', 'age': 25, 'address': 'Sao Paulo', 'height': 1.80}
print(dict(me))
print(type(me))

print(me['name'])
me['name'] = "Marcelo"
del me['name']
me.pop('height', None)
print(me)

#.get() method
# Read the value of a key that does not exist in the dictionary
choc_price = products.get('Chocolate',15)
# Print the value
print('Chocolate price is TK.',choc_price)

# Read the value of a key that exists in the dictionary
juice_price = products.get('Mango Juice',15)

#.len() method
# Define a dictionary
products = { 'Fresh Oil': 500, 'Mango Juice': 30, '5 star Chocolate': 20,
'Dan Fruit Cake':50 }
# Count the total elements of the dictionary
print("Total items of the dictionary are:", len(products))

#.pop() method
# Define a dictionary
ivo = { 'Name': 'Ivo', 'Profession': 'Developer','Phone':'01866564234','Salary':300000 } 
print("\nThe content of the dictionary:\n",ivo)

# Read and delete a value from the dictionary if exists
print("\nThe phone no is:", ivo.pop('Phone'))

# Print the dictionary after pop
print("\nThe content of the dictionary after pop:\n",ivo)

# Read a key of the dictionary that does not exist
print("\nThe phone no is:", ivo.pop('Phone','01766345234'))

#.update() method
# Define two dictionaries
dict1 = {'01117856': 2.97, '01113456': 3.69, '01118734': 3.89}
dict2 = {'01113456': 3.33, '011113423': 3.98}

# Print the dict1
print("The content of the first dictionary before update:\n", dict1)

# Update dict1 by dict2
dict1.update(dict2)

# Print the dict1 after update
print("The content of the first dictionary after update:\n", dict1)


#.copy() method
# Define a dictionary
dict1 = {'01117856': 2.97, '01113456': 3.69, '01118734': 3.89}
# Create a copy of the dictionary
dict2 = dict1.copy()

# Update a value of the key of the copied dictionary
dict2['01118734'] = 3.99

# Print the original dictionary
print("The content of the original dictionary:\n", dict1)
# Print the copied dictionary
print("The content of the copied dictionary:\n", dict2)

#.sorted() method
# Define a dictionary
dictvar = {567: 3.97, 345: 2.69, 745: 3.89}

# Sort the keys of the dictionary
sorted_key = sorted(dictvar)

# Print the sorted keys
print("The content of the sorted key:\n", sorted_key)


#clear() method
# Define a dictionary
dictvar = {1001: 3.97, 1002: 2.69, 1003: 3.89}

# Print the content of the dictionary
print("The content of the dictionary:\n", dictvar)

# Remove all items of the dictionary
dictvar.clear()

# Print the dictionary after clear
print("The content of the dictionary:\n", dictvar)