def test():
  print("This is a test function")
test()


def displayName(name, age):
  print ("Hello, my name is:", name, "and my age is: ", age)

displayName("Pedro", 25)  

def sum(number1, number2):
  sum =  number1 + number2
  result = "The result is"
  return print(result, sum)

first_number = int(input("Enter the first number\n"))
second_number = int(input("Enter the second number\n"))

sum(first_number,second_number)