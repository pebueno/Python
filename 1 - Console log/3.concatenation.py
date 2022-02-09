firstName = "Pedro Ivo"
lastName = "Bueno Sartório"
age = 25
height = 1.80

#Types of concatenation
print( "My name is " + firstName, "my last name is " + lastName,"and my age and height are " + str(age), str(height))
print ("My name is " + firstName + f" I have {age:,.2f} and my height is {height:.2f}")
print ("My name is {}, I have {:.2f} and my height is {}".format(firstName,age,height))